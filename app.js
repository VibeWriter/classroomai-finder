const T=window.TOOLS,F={task:"tasks",level:"levels",price:"price",lms:"lms"},sel={};
const vals=k=>[...new Set(T.flatMap(t=>[].concat(t[F[k]])))].sort();
let h="";for(const k in F){h+=`<h4>${k.toUpperCase()}</h4>`+vals(k).map(v=>`<label><input type="checkbox" data-k="${k}" value="${v}"> ${v}</label>`).join("")}
h+=`<h4>APPROVAL</h4><label><input type="checkbox" id="appr"> Has a district approval</label>`;
document.getElementById("filters").innerHTML=h;
document.querySelectorAll("input").forEach(i=>i.addEventListener("input",render));
function render(){const q=document.getElementById("q").value.toLowerCase();
 for(const k in F)sel[k]=[...document.querySelectorAll(`input[data-k=${k}]:checked`)].map(i=>i.value);
 const r=T.filter(t=>(!q||JSON.stringify([t.name,t.tasks,t.levels,t.lms]).toLowerCase().includes(q))
  &&Object.keys(F).every(k=>!sel[k].length||sel[k].some(v=>[].concat(t[F[k]]).includes(v)))
  &&(!appr.checked||t.approvals.length)&&(!esl.checked||t.esl));
 count.textContent=r.length+" tools";
 grid.innerHTML=r.map(t=>`<div class="card"><h3><a href="tool.html?id=${t.id}">${t.name}</a></h3><div>${t.tasks.map(x=>`<span class=tag>${x}</span>`).join("")}</div><p>${t.price} · ${t.levels.join(", ")}</p>${t.approvals.length?`<span class="tag ok">✓ ${t.approvals.length} district approval(s)</span>`:""}</div>`).join("")}
render();
