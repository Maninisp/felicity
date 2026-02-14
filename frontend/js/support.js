async function loadSupport() {
  const container = document.getElementById("supportContainer");
  const resultCount = document.getElementById("resultCount");

  container.innerHTML = "<p class='loading'>Loading services...</p>";

  const condition = document.getElementById("conditionFilter").value;
  const city = document.getElementById("cityFilter").value;
  const type = document.getElementById("typeFilter").value;

  // 🔥 Build params properly
  const params = { page: "support" };

  // Only add city if NOT "all"
  if (city && city !== "all") {
    params.city = city;
  }

  // Only add condition if NOT "all"
  if (condition && condition !== "all") {
    params.condition = condition;
  }

if (type && type !== "all") {
  params.type = type;
}

  try {
    const data = await fetchServices(params);
    renderSupport(data);
  } catch (error) {
    container.innerHTML = "<p class='error'>Failed to load services.</p>";
  }
}

function renderSupport(list) {
  const container = document.getElementById("supportContainer");
  const resultCount = document.getElementById("resultCount");

  resultCount.textContent = `${list.length} service(s) found`;
  container.innerHTML = "";

  if (!list || list.length === 0) {
    container.innerHTML = "<p>No services found.</p>";
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

document.getElementById("conditionFilter").addEventListener("change", loadSupport);
document.getElementById("cityFilter").addEventListener("change", loadSupport);
document.getElementById("typeFilter").addEventListener("change", loadSupport);

// Initial load
loadSupport();
