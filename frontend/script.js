async function convert() {
  const fileInput = document.getElementById("fileInput");
  const output = document.getElementById("output");

  if (!fileInput.files.length) {
    alert("Please select a file");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  output.textContent = "Processing...";

  try {
    const response = await fetch("http://127.0.0.1:5001/extract", {

      method: "POST",
      body: formData
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data.json_output, null, 2);
  } catch (error) {
    output.textContent = "Error connecting to server";
  }
}
