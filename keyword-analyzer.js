function analyzeKeywords(text) {
    const stopWords = ["the", "is", "and", "a", "to", "in", "of"];

    const words = text
        .toLowerCase()
        .replace(/[^\w\s]/g, "")
        .split(" ");

    const freq = {};

    words.forEach(word => {
        if (!stopWords.includes(word) && word !== "") {
            freq[word] = (freq[word] || 0) + 1;
        }
    });

    return Object.entries(freq)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
}

// Example
console.log(analyzeKeywords("This is a simple test. This test is only a test."));
