async function loadTraining() {
  const container = document.getElementById("trainingContainer");
  const resultCount = document.getElementById("resultCount");

  container.innerHTML = "<p class='loading'>Loading programs...</p>";

  const condition = document.getElementById("conditionFilter").value;
  const city = document.getElementById("cityFilter").value;
  const type = document.getElementById("typeFilter").value;

  const params = { page: "training" };

  if (city && city !== "all") {
    params.city = city;
  }

  if (condition && condition !== "all") {
    params.condition = condition;
  }

  if (type && type !== "all") {
    params.type = type;
  }

  try {
    const data = await fetchServices(params);
    renderTraining(data);
  } catch (error) {
    container.innerHTML = "<p class='error'>Failed to load programs.</p>";
  }
}

function renderTraining(list) {
  const container = document.getElementById("trainingContainer");
  const resultCount = document.getElementById("resultCount");

  resultCount.textContent = `${list.length} program(s) found`;
  container.innerHTML = "";

  if (!list || list.length === 0) {
    container.innerHTML = "<p>No programs found.</p>";
    return;
  }

  list.forEach(s => {
    container.innerHTML += `
      <div class="service-card">
        <h3>${s.name}</h3>
        <p>Category: ${s.type}</p>
        <p>City: ${s.city}</p>
      </div>
    `;
  });
}

document.getElementById("conditionFilter").addEventListener("change", loadTraining);
document.getElementById("cityFilter").addEventListener("change", loadTraining);
document.getElementById("typeFilter").addEventListener("change", loadTraining);

loadTraining();