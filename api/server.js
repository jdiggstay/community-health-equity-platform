const express = require("express");
const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
    res.send("Community Health Equity Platform API");
});

app.get("/communities", (req, res) => {
    res.json([
        {
            community: "North Lawndale",
            diabetes_rate: 14.2,
            clinic_count: 4
        },
        {
            community: "Austin",
            diabetes_rate: 12.8,
            clinic_count: 7
        },
        {
            community: "Hyde Park",
            diabetes_rate: 7.4,
            clinic_count: 3
        }
    ]);
});

app.listen(PORT, () => {
    console.log('API running at http://localhost:${PORT}');
});