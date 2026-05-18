function App() {
  return (
    <div style={{ maxWidth: "900px", margin: "40px auto", fontFamily: "Arial, sans-serif" }}>
      <h1>Community Health Equity Platform</h1>

      <p>
        A healthcare analytics platform designed to identify
        high-risk communities and improve resource allocation.
      </p>

      <ul>
        <li>Risk scoring</li>
        <li>Trend analysis</li>
        <li>Resource gap identification</li>
        <li>Interactive dashboards</li>
      </ul>

      <button onClick={() => alert("Welcome to the Community Health Equity Platform!")}>
        Explore the Platform
      </button>
    </div>
  );
}

export default App;