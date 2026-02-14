const API_BASE = window.API_BASE || "http://127.0.0.1:5000/services";

async function fetchServices(params = {}) {
  const query = new URLSearchParams(params).toString();
  const url = `${API_BASE}?${query}`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    return await response.json();

  } catch (error) {
    console.error("API ERROR:", error);
    throw error;
  }
}

console.log("API BASE:", window.API_BASE);