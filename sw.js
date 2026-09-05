/* Sentence Builder - offline copy.
   After the first visit the whole app is kept on the phone. The page is
   served from that copy instantly (so it opens with no internet at all),
   and a fresh copy is fetched in the background whenever there IS
   internet, so students get your updates on their next open.
   Change CACHE (for example to v2.5) whenever you upload a new version. */
var CACHE = 'sentence-builder-v2.5';
var PAGE = './index.html';
var ASSETS = [PAGE, './comparative-essay.html', './sandwich-essay.html', './manifest.webmanifest', './icon-180.png', './icon-192.png', './icon-512.png'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function offlineFallback() {
  return new Response('Offline and no saved copy yet. Open once with internet.', { status: 503, headers: { 'Content-Type': 'text/plain' } });
}

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  var isPage = req.mode === 'navigate' || url.pathname.endsWith('/index.html') || url.pathname.endsWith('/');
  if (isPage) {
    /* serve the saved copy at once; refresh it in the background when online */
    var refresh = fetch(req).then(function (res) {
      if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(PAGE, copy); }); }
      return res;
    }).catch(function () { return null; });
    e.waitUntil(refresh);
    e.respondWith(caches.match(PAGE).then(function (cached) {
      return cached || refresh.then(function (r) { return r || offlineFallback(); });
    }));
  } else {
    e.respondWith(caches.match(req).then(function (r) {
      return r || fetch(req).then(function (res) {
        if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
        return res;
      });
    }));
  }
});
