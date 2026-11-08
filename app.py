
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Diwali 🪔",
    page_icon="🪔",
    layout="wide"
)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #160b20;
    color: white;
    font-family: Georgia, serif;
    overflow-x: hidden;
}

.main {
    min-height: 100vh;
    background:
    radial-gradient(ellipse at 50% 40%, #57213c 0%, transparent 65%),
    linear-gradient(160deg, #160b20, #29102c, #10091b);
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 25px 15px 45px;
}

#fireworks {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5;
}

.stars {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background-image:
    radial-gradient(2px 2px at 20% 20%, #ffe5a1 50%, transparent),
    radial-gradient(2px 2px at 70% 15%, #fff0c4 50%, transparent),
    radial-gradient(2px 2px at 85% 45%, #ffe5a1 50%, transparent),
    radial-gradient(2px 2px at 15% 70%, #fff0c4 50%, transparent),
    radial-gradient(2px 2px at 60% 85%, #ffe5a1 50%, transparent);
    opacity: .7;
}

.lights {
    display: flex;
    justify-content: space-around;
    max-width: 700px;
    margin: 0 auto 45px;
    padding: 15px 0;
    border-top: 2px solid #bd8745;
    position: relative;
}

.light {
    width: 11px;
    height: 17px;
    border-radius: 50%;
    background: #ffcc69;
    box-shadow: 0 0 12px #ffb52e, 0 0 28px #ff9c29;
    animation: glow 1.5s infinite alternate;
}

.light:nth-child(even) {
    animation-delay: .6s;
}

@keyframes glow {
    from { opacity: .5; }
    to {
        opacity: 1;
        box-shadow: 0 0 20px #ffcb68, 0 0 40px #ff9c29;
    }
}

.top-label {
    color: #f6ca86;
    letter-spacing: 5px;
    font-size: 11px;
    margin-bottom: 25px;
    text-transform: uppercase;
}

h1 {
    font-size: clamp(43px, 9vw, 76px);
    line-height: 1.15;
    color: #ffe5a7;
    text-shadow: 0 0 15px #d68c40, 0 0 45px #b85c36;
    font-weight: normal;
}

.subtitle {
    color: #f2c6a0;
    font-size: 17px;
    margin-top: 18px;
    letter-spacing: 1px;
}

.diya-area {
    margin: 35px auto 25px;
    position: relative;
    width: 180px;
    height: 170px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.diya {
    font-size: 105px;
    filter: drop-shadow(0 0 20px #ff9e32);
    animation: diyaGlow 2s infinite alternate;
}

@keyframes diyaGlow {
    from { filter: drop-shadow(0 0 10px #ff9e32); }
    to { filter: drop-shadow(0 0 35px #ffcf65); }
}

.message {
    max-width: 570px;
    margin: 15px auto;
    color: #f7dfc8;
    font-size: 17px;
    line-height: 1.9;
    padding: 0 15px;
}

.divider {
    width: 90px;
    height: 1px;
    background: #d6a35c;
    margin: 30px auto;
}

.wish-card {
    max-width: 520px;
    margin: 35px auto;
    padding: 28px 22px;
    border: 1px solid rgba(255,207,133,.35);
    border-radius: 18px;
    background: rgba(255,255,255,.045);
    box-shadow: 0 10px 50px rgba(0,0,0,.2);
}

.wish-card h2 {
    color: #ffda9a;
    font-size: 25px;
    font-weight: normal;
    margin-bottom: 15px;
}

.wish-card p {
    color: #eecdb5;
    line-height: 1.8;
    font-size: 15px;
}

button {
    border: 1px solid #ffe1a0;
    background: linear-gradient(135deg, #e8a54e, #b96835);
    color: #321323;
    border-radius: 50px;
    padding: 16px 35px;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 1px;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(255,170,67,.35);
    transition: .3s;
    margin: 18px auto;
}

button:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 35px rgba(255,170,67,.7);
}

#surprise {
    display: none;
    color: #ffe4ad;
    font-size: 19px;
    line-height: 1.8;
    margin: 25px auto;
    max-width: 500px;
    animation: appear 1s ease;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.footer {
    margin-top: 55px;
    color: #d7ad91;
    font-size: 13px;
    line-height: 2;
}

.signature {
    color: #ffe0a2;
    font-size: 15px;
    margin-top: 8px;
}

@media(max-width: 600px) {
    .main {
        padding-top: 20px;
    }

    .lights {
        margin-bottom: 38px;
    }

    .message {
        font-size: 15px;
    }

    .wish-card {
        margin: 25px 5px;
    }
}
</style>
</head>

<body>

<canvas id="fireworks"></canvas>

<div class="main">

<div class="stars"></div>

<div class="lights">
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
    <span class="light"></span>
</div>

<div class="top-label">
    A festival of lights, love and happiness
</div>

<h1>Happy<br>Diwali!</h1>

<p class="subtitle">
    ✨ May your life shine brighter ✨
</p>

<div class="diya-area">
    <div class="diya">🪔</div>
</div>

<div class="message">
    Some festivals are more than celebrations.
    They bring people closer, fill our homes with
    warmth and remind us to spread happiness.
    <br><br>
    So, I made this little corner of light and
    happiness to wish you all a beautiful Diwali.
</div>

<div class="divider"></div>

<div class="wish-card">
    <h2>A Little Wish For You ❤️</h2>

    <p>
        May every diya bring a new hope into your life.
        May your home be filled with laughter,
        your heart with peace, and your days with
        endless happiness.
        <br><br>
        Wishing you and your family prosperity,
        good health and countless beautiful moments.
    </p>
</div>

<button onclick="lightDiya()">
    🪔 Light a Diya
</button>

<div id="surprise">
    ✨ A little light can brighten the darkest night. ✨
    <br><br>
    Keep smiling, keep shining and keep spreading
    happiness wherever you go.
    <br><br>
    Once again, a very Happy Diwali! ❤️
</div>

<div class="footer">
    Made with love, just to spread a little happiness.
    <div class="signature">
        ❤️ Made with a little bit of code by Deep.
    </div>
    <br>
    शुभ दीपावली 🪔
</div>

</div>

<script>
const canvas = document.getElementById("fireworks");
const ctx = canvas.getContext("2d");

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

resize();
window.addEventListener("resize", resize);

let particles = [];

function burst(x, y) {
    for (let i = 0; i < 65; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 5 + 1;

        particles.push({
            x: x,
            y: y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 100,
            color: ["#ffd166", "#ff9f43", "#fff0b3",
                    "#ff6b81", "#ffffff"][Math.floor(Math.random()*5)]
        });
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.025;
        p.life -= 1.5;

        ctx.globalAlpha = Math.max(0, p.life / 100);
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
        ctx.fill();
    });

    particles = particles.filter(p => p.life > 0);

    ctx.globalAlpha = 1;
    requestAnimationFrame(animate);
}

animate();

function lightDiya() {
    document.getElementById("surprise").style.display = "block";

    const diya = document.querySelector(".diya");
    diya.style.transform = "scale(1.2)";
    diya.style.transition = "1s";

    burst(window.innerWidth / 2, window.innerHeight / 2);

    setTimeout(() => {
        burst(window.innerWidth * .25, window.innerHeight * .35);
        burst(window.innerWidth * .75, window.innerHeight * .35);
    }, 350);

    document.getElementById("surprise").scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}
</script>

</body>
</html>
"""

components.html(html, height=1250, scrolling=True)
"""

components.html(html, height=1250, scrolling=True)
