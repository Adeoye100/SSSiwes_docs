const CACHE_NAME = 'sanfaani-docs-v1';

// Install event - we can optionally pre-cache some assets, but we'll use a dynamic strategy.
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      // Pre-cache main page
      return cache.addAll([
        './',
        './index.html'
      ]);
    })
  );
  self.skipWaiting();
});

// Activate event - clean up old caches if any
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(name => name !== CACHE_NAME).map(name => caches.delete(name))
      );
    })
  );
  self.clients.claim();
});

// Fetch event - Stale-while-revalidate strategy
self.addEventListener('fetch', event => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;
  
  // Skip chrome-extension requests or non-http protocols
  if (!event.request.url.startsWith('http')) return;

  event.respondWith(
    caches.open(CACHE_NAME).then(async cache => {
      // Try to get the response from the cache
      const cachedResponse = await cache.match(event.request);
      
      // Fetch the network response in the background
      const networkResponsePromise = fetch(event.request).then(networkResponse => {
        // If valid response, clone and update cache
        if (networkResponse && networkResponse.status === 200 && networkResponse.type !== 'opaque') {
          cache.put(event.request, networkResponse.clone());
        }
        return networkResponse;
      }).catch(() => {
        // Network failed (offline). We rely on the cachedResponse if it exists.
      });

      // Return cached response immediately if available, otherwise wait for network
      return cachedResponse || networkResponsePromise;
    })
  );
});
