
import base64
import os

# 1. Setup Data
members = [
    {
        "name": "Harlin Janold C R",
        "role_meta": "Team Leader • ECE",
        "role_main": "Team Leader & System Architect",
        "email": "janoldjanocr@gmail.com",
        "year": "2025-26",
        "skills": ["Solution Design & Integration", "Mentor Coordination", "Hardware-Software-AI Integration"],
        "links": [
            ("GitHub", "https://github.com/harlinjanold"),
            ("LinkedIn", "https://www.linkedin.com/in/harlinjanold/")
        ],
        "img": "harlin_linkedin.jpg"
    },
    {
        "name": "Febin Anto K K",
        "role_meta": "Computer Science",
        "role_main": "Embedded Hardware & IoT Engineer",
        "email": "febinanto61@gmail.com",
        "year": "2022-26",
        "skills": ["Sensor Integration (NIR, Camera, Force)", "PCB Design & Wiring", "Power Systems", "Device Enclosure"],
        "links": [
            ("LinkedIn", "https://www.linkedin.com/in/febinantokk")
        ],
        "img": "febin_linkedin.jpg"
    },
    {
        "name": "R J Nishmah",
        "role_meta": "AI & Data Science",
        "role_main": "AI / ML Engineer (Brix Prediction)",
        "email": "nishmah2192004@gmail.com",
        "year": "IV Year AI&DS",
        "skills": ["Dataset Creation", "NIR to °Brix Model Development", "Maturity Index Modeling", "Edge AI Deployment"],
        "links": [
            ("GitHub", "https://github.com/R-J-Nishmah"),
            ("LinkedIn", "https://in.linkedin.com/in/nishmah-r-j-8b94812a6")
        ],
        "img": "nishmah_linkedin.jpg"
    },
    {
        "name": "Jeshwin David C",
        "role_meta": "AI & Data Science",
        "role_main": "Software & UI/UX Developer",
        "email": "jeshwindavid5@gmail.com",
        "year": "3rd Year AI&DS",
        "skills": ["Raspberry Pi Software", "User Interface Design", "Bilingual Workflow", "QR & Data Logging"],
        "links": [
            ("LinkedIn", "https://www.linkedin.com/in/jeshwin-david-6b2283320")
        ],
        "img": "jeshwin_linkedin.jpg"
    },
    {
        "name": "Sree Lasha L",
        "role_meta": "Electrical & Electronics",
        "role_main": "Field Testing & Agriculture Domain Specialist",
        "email": "lashasree88@gmail.com",
        "year": "2025-26",
        "skills": ["Field Trials with Farmers/Mills", "Refractometer Ground Truth Collection", "Real-Condition Validation"],
        "links": [],
        "img": "team_sree.png"
    },
    {
        "name": "Navein Shyam A S",
        "role_meta": "Electrical & Electronics",
        "role_main": "Documentation, Operations & IP Coordinator",
        "email": "naveinshyam99@gmail.com",
        "year": "2022-26",
        "skills": ["Presentations & Reports", "Videos & Timelines", "BoM & Costing", "Novelty & IP Documentation"],
        "links": [
            ("LinkedIn", "http://linkedin.com/in/navein-shyam-427a7226b")
        ],
        "img": "team_navein.png"
    }
]

base_dir = '/Users/griffinannshuals/Downloads/Brixometer Portfoio/assets'

def get_b64(filename):
    path = os.path.join(base_dir, filename)
    try:
        with open(path, 'rb') as f:
            data = f.read()
            ext = filename.split('.')[-1]
            mime = 'image/jpeg' if ext in ['jpg', 'jpeg'] else 'image/png'
            return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return ""

# 2. Build template parts
cards_html = ""
for m in members:
    img_src = get_b64(m['img'])
    
    skills_html = ""
    for s in m['skills']:
        skills_html += f"<li>{s}</li>"
        
    links_html = ""
    for label, url in m['links']:
        links_html += f'<a href="{url}" target="_blank">{label}</a>'
    
    card = f"""
    <div class="team-card">
        <div class="card-inner">
            <div class="img-wrapper">
                <img src="{img_src}" alt="{m['name']}">
            </div>
            <div class="role-badge">{m['role_meta']}</div>
            <h3>{m['name']}</h3>
            <div class="main-role">{m['role_main']}</div>
            
            <div class="info-group">
                <div class="email">{m['email']}</div>
                <div class="year">Batch: {m['year']}</div>
            </div>

            <div class="divider"></div>
            
            <ul class="skills">
                {skills_html}
            </ul>

            <div class="social-row">
                {links_html}
            </div>
        </div>
    </div>
    """
    cards_html += card

# 3. HTML Content
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brixometer Team | The Minds Behind the Innovation</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #00C853;     /* Green from Portfolio */
            --dark-bg: #0a0a0a;
            --card-bg: rgba(255, 255, 255, 0.03);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-main: #ffffff;
            --text-muted: #888888;
            --gradient-1: linear-gradient(135deg, #00C853 0%, #B2FF59 100%);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background-color: var(--dark-bg);
            color: var(--text-main);
            font-family: 'Outfit', sans-serif;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 200, 83, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(0, 100, 255, 0.1) 0%, transparent 40%);
            min-height: 100vh;
        }}

        /* Navbar */
        nav {{
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(10px);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 100;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        .brand {{
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-dot {{
            width: 12px;
            height: 12px;
            background: var(--primary);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--primary);
        }}

        /* Hero */
        .hero {{
            text-align: center;
            padding: 160px 20px 80px;
            position: relative;
        }}

        h1 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(3rem, 6vw, 5rem);
            line-height: 1;
            margin-bottom: 20px;
            background: linear-gradient(to right, #fff, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }}

        .team-name {{
            color: var(--primary);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
            display: block;
            font-size: 0.9rem;
        }}

        /* Grid */
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 40px 100px;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
        }}

        /* Card STUNNING Styles */
        .team-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 40px 30px;
            position: relative;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(20px);
            overflow: hidden;
        }}

        .team-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 100%);
            opacity: 0;
            transition: 0.4s;
        }}

        .team-card:hover {{
            transform: translateY(-10px) scale(1.02);
            border-color: rgba(0, 200, 83, 0.3);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}

        .team-card:hover::before {{
            opacity: 1;
        }}

        .img-wrapper {{
            width: 120px;
            height: 120px;
            margin: 0 auto 25px;
            border-radius: 50%;
            padding: 4px;
            background: linear-gradient(to bottom, var(--primary), transparent);
            position: relative;
        }}

        .img-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid var(--dark-bg);
            filter: grayscale(20%);
            transition: 0.4s;
        }}

        .team-card:hover img {{
            filter: grayscale(0%);
            transform: scale(1.05);
        }}

        .role-badge {{
            text-align: center;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--primary);
            margin-bottom: 10px;
            font-weight: 700;
        }}

        h3 {{
            text-align: center;
            font-size: 1.6rem;
            margin-bottom: 8px;
            font-family: 'Space Grotesk', sans-serif;
        }}

        .main-role {{
            text-align: center;
            color: #ccc;
            margin-bottom: 25px;
            font-weight: 300;
            font-size: 1rem;
        }}

        .info-group {{
            text-align: center;
            font-size: 0.9rem;
            color: var(--text-muted);
            margin-bottom: 20px;
        }}

        .email {{
            color: #fff;
            margin-bottom: 4px;
        }}

        .divider {{
            height: 1px;
            background: rgba(255,255,255,0.1);
            margin: 20px 0;
        }}

        .skills {{
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            justify-content: center;
            margin-bottom: 25px;
        }}

        .skills li {{
            font-size: 0.8rem;
            padding: 4px 12px;
            background: rgba(255,255,255,0.05);
            border-radius: 100px;
            color: #aaa;
            border: 1px solid rgba(255,255,255,0.05);
        }}

        .social-row {{
            display: flex;
            justify-content: center;
            gap: 15px;
        }}

        .social-row a {{
            color: #fff;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            font-size: 0.85rem;
            transition: 0.2s;
            border: 1px solid transparent;
        }}

        .social-row a:hover {{
            background: var(--primary);
            color: #000;
            font-weight: 600;
            box-shadow: 0 0 15px rgba(0, 200, 83, 0.4);
        }}

        footer {{
            text-align: center;
            padding: 40px;
            border-top: 1px solid rgba(255,255,255,0.05);
            color: var(--text-muted);
            font-size: 0.9rem;
        }}

    </style>
</head>
<body>

    <nav>
        <div class="brand">
            <div class="brand-dot"></div>
            BRIXOMETER
        </div>
    </nav>

    <header class="hero">
        <span class="team-name">Team CRYOCIVIC</span>
        <h1>Meet the Creators</h1>
        <p class="subtitle">
            A multidisciplinary collective from Mar Ephraem College of Engineering, united by a passion for agricultural innovation and AI.
        </p>
    </header>

    <div class="container">
        <div class="grid">
            {cards_html}
        </div>
    </div>

    <footer>
        &copy; 2025 Team CRYOCIVIC • SIH152264<br>
        <span style="opacity: 0.5; margin-top: 10px; display: inline-block;">Grand Finale Qualifier</span>
    </footer>

</body>
</html>
"""

with open('/Users/griffinannshuals/Downloads/Brixometer Portfoio/team.html', 'w') as f:
    f.write(html_content)

print("team.html has been successfully rebuilt with embedded assets.")
