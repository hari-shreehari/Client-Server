// Base URL of your FastAPI backend
const API_BASE = "http://localhost:8000";

// ----- 1) Submit Name + DOB -----
document.getElementById("submitUserBtn").addEventListener("click", async () => {
  const name = document.getElementById("nameInput").value.trim();
  const dob = document.getElementById("dobInput").value; // yyyy-MM-dd

  // Basic validation
  if (!name || !dob) {
    document.getElementById("userMsg").textContent = "Please fill both fields.";
    return;
  }

  try {
    const resp = await fetch(API_BASE + "/submit-data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, dob }),
    });

    if (!resp.ok) {
      throw new Error("Server returned " + resp.status);
    }

    const data = await resp.json();
    document.getElementById("userMsg").textContent = data.message;
  } catch (err) {
    console.error(err);
    document.getElementById("userMsg").textContent = "Error: Could not submit.";
  }
});

// ----- 2) Add 2 Numbers (Client-Side) -----
document.getElementById("addBtn").addEventListener("click", () => {
  const aVal = document.getElementById("numA").value;
  const bVal = document.getElementById("numB").value;

  // Parse to floats (or integers)
  const a = parseFloat(aVal);
  const b = parseFloat(bVal);

  if (isNaN(a) || isNaN(b)) {
    document.getElementById("sumResult").textContent =
      "Please enter valid numbers.";
    return;
  }

  // Compute sum entirely in the browser:
  const sum = a + b;
  document.getElementById("sumResult").textContent = "Sum = " + sum;
});

