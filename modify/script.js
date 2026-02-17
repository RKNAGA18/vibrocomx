// VibrocomX Script - Core Logic
// Author: Antigravity

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize AOS (Animate On Scroll)
    // Dynamic import if we were using modules, but here relies on CDN in HTML
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            once: true,
            easing: 'ease-out-cubic'
        });
    }

    // 2. Countdown Timer Logic
    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {
        // Set a future date (e.g., 2 days from now)
        const targetDate = new Date();
        targetDate.setDate(targetDate.getDate() + 2);
        targetDate.setHours(20, 0, 0, 0); // 8 PM

        function updateCountdown() {
            const now = new Date();
            const difference = targetDate - now;

            if (difference <= 0) {
                countdownElement.innerText = "LIVE NOW";
                countdownElement.classList.add('text-red-500', 'animate-pulse');
                return;
            }

            const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((difference % (1000 * 60)) / 1000);

            countdownElement.innerText =
                `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        }

        setInterval(updateCountdown, 1000);
        updateCountdown(); // Initial call
    }

    // 3. Glitch Effect Randomizer (Optional extra flair)
    const glitches = document.querySelectorAll('.glitch-text');
    glitches.forEach(glitch => {
        setInterval(() => {
            if (Math.random() > 0.95) {
                glitch.style.setProperty('--primary-red', '#fff');
                setTimeout(() => {
                    glitch.style.setProperty('--primary-red', '#ff003c');
                }, 50);
            }
        }, 1000);
    });

    // 4. Matrix/Cyber Rain Canvas Effect (Simple)
    const canvas = document.createElement('canvas');
    canvas.id = 'bg-canvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '-1';
    canvas.style.opacity = '0.1';
    canvas.style.pointerEvents = 'none';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    const cols = Math.floor(width / 20);
    const ypos = Array(cols).fill(0);

    function matrix() {
        ctx.fillStyle = '#0001';
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = '#ff003c';
        ctx.font = '15pt monospace';

        ypos.forEach((y, index) => {
            const text = String.fromCharCode(Math.random() * 128);
            const x = index * 20;
            ctx.fillText(text, x, y);
            if (y > 100 + Math.random() * 10000) ypos[index] = 0;
            else ypos[index] = y + 20;
        });
    }

    setInterval(matrix, 50);

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    console.log("VibrocomX Systems Online.");
});