const generateBtn = document.getElementById("generateBtn");
const copyBtn = document.getElementById("copyBtn");
const output = document.getElementById("output");
const status = document.getElementById("status");

generateBtn.addEventListener("click", async () => {
    const topic = document.getElementById("topic").value.trim();

    if (!topic) {
        status.textContent = "Please enter a topic first.";
        return;
    }

    status.textContent = "Generating...";
    generateBtn.disabled = true;

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                content_type: document.getElementById("contentType").value,
                topic,
                audience: document.getElementById("audience").value,
                tone: document.getElementById("tone").value,
                length: document.getElementById("length").value
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        output.textContent = data.content;
        status.textContent = "Content generated successfully.";
    } catch (error) {
        status.textContent = error.message;
    } finally {
        generateBtn.disabled = false;
    }
});

copyBtn.addEventListener("click", async () => {
    await navigator.clipboard.writeText(output.textContent);
    copyBtn.textContent = "Copied!";
    setTimeout(() => copyBtn.textContent = "Copy", 1500);
});
