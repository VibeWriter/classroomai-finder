import json
H="https://resources.finalsite.net/images/v1777472784/houstonisdorg/ffvo6lng6pttnchgfzgh/25-26HISDAIGuidebook.pdf"
S="https://www.usd305.com/about/school-and-community-information/ai-guidelines/genai-tool-approved-list"
T="https://www.tusd.org/educational-services/ai/district-approved-ai-tools"
A="https://www.apsva.us/digital-learning-innovation/aps-ai-digital-learning-hub/instructional-toolkit/"
def ap(*xs): return [{"district":d,"note":n,"source":u} for d,n,u in xs]
hou=("Houston ISD (TX)","Approved for teacher use with students",H)
sal=("Salina USD 305 (KS)","On district's vetted GenAI list (per-level status in table)",S)
tor=("Torrance USD (CA)","District-approved / piloted",T)
arl=("Arlington Public Schools (VA)","In APS approved instructional toolkit",A)
R=[
("MagicSchool","https://www.magicschool.ai",["lesson planning","differentiation","rubrics","feedback","admin/communication"],["K-12"],"Freemium","Free teacher plan; paid Plus/enterprise",["Google Classroom","Canvas","Schoology"],ap(sal),False),
("Brisk Teaching","https://www.briskteaching.com",["feedback","differentiation","lesson planning","assessment"],["K-12","college"],"Freemium","Free Chrome extension; Pro/school plans",["Google Classroom","Canvas"],[],False),
("Diffit","https://web.diffit.me",["differentiation","leveled reading","assessment"],["K-12","ESL"],"Freemium","Free tier; Premium/school plans",["Google Classroom","Canvas"],[],True),
("SchoolAI","https://schoolai.com",["student AI spaces","lesson planning","differentiation","feedback"],["K-12"],"Freemium","Free teacher tier; school plans",["Google Classroom","Canvas","Schoology"],ap(sal,tor,arl),False),
("Eduaide.ai","https://www.eduaide.ai",["lesson planning","worksheets","rubrics","feedback"],["K-12","ESL"],"Freemium","Free tier; Pro",[],[],True),
("Khanmigo","https://www.khanmigo.ai",["tutoring","lesson planning"],["K-12"],"Free for teachers","Free for US teachers; student plans paid",["Google Classroom","Canvas","Schoology"],[],False),
("NotebookLM","https://notebooklm.google.com",["research","study guides","audio summaries"],["K-12","college","adult"],"Free","Free; included with Google Workspace for Education",["Google Classroom"],ap(tor),False),
("Google Gemini","https://gemini.google.com",["general assistant","lesson planning","feedback"],["K-12","college","adult","ESL"],"Freemium","Free; Workspace for Education add-ons",["Google Classroom"],ap(hou,sal,tor,arl),True),
("Microsoft Copilot","https://copilot.microsoft.com",["general assistant","lesson planning","admin/communication"],["K-12","college","adult"],"Freemium","Free Copilot Chat; M365 Copilot paid",["Microsoft Teams"],ap(hou),False),
("Microsoft Reading Coach","https://coach.microsoft.com",["reading practice","literacy"],["K-12","ESL"],"Free","Free",["Microsoft Teams"],ap(hou),True),
("ChatGPT","https://chatgpt.com",["general assistant","lesson planning","speaking practice"],["college","adult","ESL"],"Freemium","Free; Plus/Edu paid",[],ap(sal),True),
("Claude","https://claude.ai",["general assistant","lesson planning","presentations"],["college","adult"],"Freemium","Free; Pro/Education paid",["Canvas"],ap(sal),False),
("Consensus","https://consensus.app",["research"],["college","adult"],"Freemium","Free tier; Premium",[],ap(sal),False),
("Canva for Education","https://www.canva.com/education/",["presentations","design"],["K-12"],"Free for K-12","Free for eligible K-12 teachers and students",["Google Classroom","Canvas","Schoology","Microsoft Teams"],ap(sal),False),
("Adobe Express (Education)","https://www.adobe.com/express/education",["design","presentations"],["K-12","college"],"Free for K-12","Free for K-12 schools",["Google Classroom","Canvas","Schoology"],ap(hou),False),
("Curipod","https://curipod.com",["interactive lessons","presentations","assessment"],["K-12"],"Freemium","Free tier; school plans",["Google Classroom","Microsoft Teams"],[],False),
("Wayground (formerly Quizizz)","https://wayground.com",["assessment","quizzes"],["K-12"],"Freemium","Free basic; paid tiers",["Google Classroom","Canvas","Schoology"],[],False),
("Kahoot!","https://kahoot.com",["quizzes","engagement"],["K-12","college","adult"],"Freemium","Free basic; paid tiers",["Microsoft Teams"],[],True),
("Gamma","https://gamma.app",["presentations"],["college","adult"],"Freemium","Free credits; Plus/Pro",[],[],False),
("HeyGen","https://www.heygen.com",["video creation","dubbing/translation"],["college","adult","ESL"],"Freemium","Limited free plan; paid tiers",[],[],True),
("Snorkl","https://snorkl.app",["feedback","assessment"],["K-12"],"Freemium","Free tier; school plans",["Google Classroom"],[],False),
("Conker","https://www.conker.ai",["assessment","quizzes"],["K-12"],"Freemium","Free tier; paid",["Google Classroom"],[],False),
("Formative","https://www.formative.com",["assessment","feedback"],["K-12"],"Freemium","Free basic; paid",["Google Classroom","Canvas","Schoology"],[],False),
("Mizou","https://mizou.com",["student AI chatbots","tutoring"],["K-12"],"Freemium","Free tier; paid",["Google Classroom"],[],False),
("SlidesAI","https://www.slidesai.io",["presentations"],["K-12","college"],"Freemium","Free tier; paid",["Google Slides"],[],False),
("ELSA Speak","https://elsaspeak.com",["pronunciation","speaking practice"],["adult","ESL"],"Freemium","Free limited; Pro subscription",[],[],True),
("Promova","https://promova.com",["speaking practice","vocabulary"],["adult","ESL"],"Freemium","Free limited; Premium",[],[],True),
("Speak","https://www.speak.com",["speaking practice"],["adult","ESL"],"Paid (trial)","Free trial; subscription",[],[],True),
("ESLvideo / Neo English","https://eslvideo.com",["listening","speaking practice","assessment"],["adult","ESL"],"Freemium","Teacher accounts; see site for plans",["Canvas"],[],True),
("Gliglish","https://gliglish.com",["speaking practice"],["adult","ESL"],"Freemium","Free daily minutes; paid",[],[],True),
("Lesson Mate AI","https://www.lessonmate.ai",["lesson planning","worksheets"],["ESL"],"Freemium","See site",[],[],True),
]
out=[]
for n,u,t,l,p,f,lms,a,esl in R:
    out.append(dict(id=n.lower().replace(" ","-").replace("/","-").replace("!","").replace("(","").replace(")","").replace(".",""),name=n,url=u,tasks=t,levels=l,price=p,free_tier=f,lms=lms,approvals=a,esl=esl))
json.dump(out,open("data/tools.json","w"),indent=1)
