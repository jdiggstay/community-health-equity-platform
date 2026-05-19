const express = require("express");
const { Pool } = require("pg");

const app = express();
const PORT = 3000;

const pool = new Pool({
  database: "healthcare_analytics"
});

app.get("/", (req, res) => {
  res.send("Community Health Equity Platform API");
});

app.get("/communities", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT * FROM communities ORDER BY diabetes_rate DESC"
    );
    res.json(result.rows);
  } catch (error) {
    console.error(error);
    res.status(500).send("Database error");
  }
});

app.listen(PORT, () => {
  console.log(`API running at http://localhost:${PORT}`);
});