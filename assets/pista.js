// Pista policies: section cards, numbered headings, contents + scrollspy, reading progress,
// theme toggle, copy-link anchors, back-to-top. Everything is progressive: without JS the page
// is the plain, fully readable document.
(function () {
  "use strict";
  var doc = document.getElementById("content");
  if (!doc) return;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function slug(text) {
    return text.toLowerCase().replace(/&/g, " and ").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  // 1. Group each h2 with the content after it into a card.
  var headings = Array.prototype.slice.call(doc.querySelectorAll(":scope > h2"));
  var count = 0;
  var sections = headings.map(function (h2) {
    var section = document.createElement("section");
    section.className = "section";
    h2.parentNode.insertBefore(section, h2);
    var node = h2;
    while (node && !(node !== h2 && node.tagName === "H2")) {
      var next = node.nextSibling;
      section.appendChild(node);
      node = next;
    }

    var label = h2.textContent.replace(/^\s*\d+\.\s+/, "").trim();
    if (!h2.id) h2.id = slug(label);
    var isSummary = /^summary$/i.test(label);
    if (isSummary) {
      section.classList.add("summary");
      h2.textContent = label;
    } else {
      count += 1;
      h2.textContent = "";
      var num = document.createElement("span");
      num.className = "num";
      num.setAttribute("aria-hidden", "true");
      num.textContent = count;
      h2.appendChild(num);
      h2.appendChild(document.createTextNode(label));
    }

    var anchor = document.createElement("a");
    anchor.className = "anchor";
    anchor.href = "#" + h2.id;
    anchor.setAttribute("aria-label", "Copy link to " + label);
    anchor.textContent = "#";
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      var url = location.href.split("#")[0] + "#" + h2.id;
      history.replaceState(null, "", "#" + h2.id);
      h2.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" });
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function () {
          anchor.classList.add("copied");
          setTimeout(function () { anchor.classList.remove("copied"); }, 1400);
        }, function () {});
      }
    });
    h2.appendChild(anchor);
    return { section: section, h2: h2, label: label };
  });

  // 2. Contents (desktop sidebar + mobile dropdown).
  var lists = document.querySelectorAll(".toc-list");
  sections.forEach(function (s) {
    lists.forEach(function (list) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "#" + s.h2.id;
      a.textContent = s.label;
      a.dataset.target = s.h2.id;
      li.appendChild(a);
      list.appendChild(li);
    });
  });
  var mobile = document.querySelector(".toc-mobile");
  if (mobile) mobile.addEventListener("click", function (e) { if (e.target.tagName === "A") mobile.open = false; });
  if (!sections.length) {
    document.querySelectorAll(".toc, .toc-mobile").forEach(function (el) { el.remove(); });
  }

  // 3. Highlight the section being read.
  var links = document.querySelectorAll(".toc-list a");
  function setActive(id) {
    links.forEach(function (a) { a.classList.toggle("active", a.dataset.target === id); });
  }
  if ("IntersectionObserver" in window && sections.length) {
    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.querySelector("h2").id] = e.isIntersecting; });
      var current = sections.filter(function (s) { return visible[s.h2.id]; })[0];
      if (current) setActive(current.h2.id);
    }, { rootMargin: "-90px 0px -55% 0px" });
    sections.forEach(function (s) { spy.observe(s.section); });
  }

  // 4. Cards fade up as they arrive.
  if (!reduceMotion && "IntersectionObserver" in window) {
    var reveal = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); reveal.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".section, .card-link").forEach(function (el) {
      el.classList.add("reveal");
      reveal.observe(el);
    });
  }

  // 5. Reading time.
  var chip = document.querySelector("[data-reading-time]");
  if (chip && sections.length) {
    var words = doc.textContent.trim().split(/\s+/).length;
    chip.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>' +
      Math.max(1, Math.round(words / 220)) + " min read";
    chip.hidden = false;
  }

  // 6. Progress bar, top bar edge, back-to-top.
  var bar = document.querySelector(".progress span");
  var topbar = document.querySelector(".topbar");
  var toTop = document.querySelector(".to-top");
  var ticking = false;
  function onScroll() {
    var max = document.documentElement.scrollHeight - innerHeight;
    var y = scrollY;
    if (bar) bar.style.setProperty("--p", max > 0 ? Math.min(1, y / max) : 0);
    if (topbar) topbar.classList.toggle("scrolled", y > 8);
    if (toTop) toTop.classList.toggle("show", y > 700);
    ticking = false;
  }
  addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () {
    scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
  });

  // 7. Theme toggle (remembers the choice; follows the phone until then).
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) toggle.addEventListener("click", function () {
    var root = document.documentElement;
    var dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("pista-theme", root.dataset.theme); } catch (e) {}
  });
})();
