async function loadResources() {
  const container = document.getElementById("resourceContainer");
  const resultCount = document.getElementById("resultCount");

  container.innerHTML = "<p class='loading'>Loading resources...</p>";

  const condition = document.getElementById("conditionFilter").value;
  const city = document.getElementById("cityFilter").value;
  const type = document.getElementById("typeFilter").value;

  const params = { page: "resource" };

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
    renderResources(data);
  } catch (error) {
    container.innerHTML = "<p class='error'>Failed to load resources.</p>";
  }
}

function renderResources(list) {
  const container = document.getElementById("resourceContainer");
  const resultCount = document.getElementById("resultCount");

  resultCount.textContent = `${list.length} resource(s) found`;
  container.innerHTML = "";

  if (!list || list.length === 0) {
    container.innerHTML = "<p>No resources found.</p>";
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

document.getElementById("conditionFilter").addEventListener("change", loadResources);
document.getElementById("cityFilter").addEventListener("change", loadResources);
document.getElementById("typeFilter").addEventListener("change", loadResources);

loadResources();