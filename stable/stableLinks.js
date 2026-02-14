// const conditionFilter = document.getElementById("conditionFilter");
// const cityFilter = document.getElementById("cityFilter");
// const searchInput = document.getElementById("searchInput");
// const cards = document.querySelectorAll(".service-card");

// let savedServices = JSON.parse(localStorage.getItem("savedServices")) || [];

// /* ---------- FILTERING ---------- */
// function filterServices() {
//   const condition = conditionFilter.value;
//   const city = cityFilter.value;
//   const search = searchInput.value.toLowerCase();

//   cards.forEach(card => {
//     const matchesCondition =
//       condition === "all" || card.dataset.condition.includes(condition);

//     const matchesCity =
//       city === "all" || card.dataset.city === city;

//     const matchesSearch =
//       card.textContent.toLowerCase().includes(search);

//     card.style.display =
//       matchesCondition && matchesCity && matchesSearch ? "block" : "none";
//   });
// }

// conditionFilter.addEventListener("change", filterServices);
// cityFilter.addEventListener("change", filterServices);
// searchInput.addEventListener("input", filterServices);

// /* ---------- LOCAL STORAGE SAVE ---------- */
// function updateButtons() {
//   cards.forEach(card => {
//     const id = card.dataset.id;
//     const button = card.querySelector(".save-btn");

//     if (savedServices.includes(id)) {
//       button.classList.add("saved");
//       button.textContent = "★ Saved";
//     } else {
//       button.classList.remove("saved");
//       button.textContent = "⭐ Save";
//     }
//   });
// }

// cards.forEach(card => {
//   const button = card.querySelector(".save-btn");
//   const id = card.dataset.id;

//   button.addEventListener("click", () => {
//     if (savedServices.includes(id)) {
//       savedServices = savedServices.filter(item => item !== id);
//     } else {
//       savedServices.push(id);
//     }

//     localStorage.setItem("savedServices", JSON.stringify(savedServices));
//     updateButtons();
//   });
// });

// updateButtons();

let servicesData = [];

fetch("services.json")
  .then(res => res.json())
  .then(data => {
    servicesData = data || [];
    displayServices(servicesData);
  })
  .catch(err => {
    console.error("JSON load error:", err);
    document.getElementById("services").innerHTML = "Error loading data.";
  });

function displayServices(list) {
  const container = document.getElementById("services");
  container.innerHTML = "";

  if (!list || list.length === 0) {
    container.innerHTML = "<p>No services found.</p>";
    return;
  }

  list.forEach(s => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <h3>${s.name || "N/A"}</h3>
      <p>${s.category || ""}</p>
      <p>${s.address || ""}</p>
      <p>📞 ${s.phone || ""}</p>
    `;

    container.appendChild(card);
  });
}

function filterServices() {
  const condition = document.getElementById("conditionFilter").value.toLowerCase();
  const city = document.getElementById("cityFilter").value.toLowerCase();
  const search = document.getElementById("searchInput").value.toLowerCase();

  const filtered = servicesData.filter(s => {
    const serviceConditions = (s.conditions || []).map(c => c.toLowerCase());
    const serviceCity = (s.city || "").toLowerCase();
    const serviceName = (s.name || "").toLowerCase();

    return (
      (condition === "all" || serviceConditions.includes(condition)) &&
      (city === "all" || serviceCity === city) &&
      serviceName.includes(search)
    );
  });

  displayServices(filtered);
}

document.getElementById("conditionFilter").addEventListener("change", filterServices);
document.getElementById("cityFilter").addEventListener("change", filterServices);
document.getElementById("searchInput").addEventListener("input", filterServices);
