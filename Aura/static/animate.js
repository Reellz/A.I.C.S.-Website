document.addEventListener("DOMContentLoaded", () => {
    const exploreSection = document.getElementById("explore");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                exploreSection.classList.add("visible");
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% of the element is visible
    });

    observer.observe(exploreSection);
});