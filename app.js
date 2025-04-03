import React, { useState, useEffect } from "react";

function App() {
  const [wardrobe, setWardrobe] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/wardrobe")
      .then((response) => response.json())
      .then((data) => setWardrobe(data));
  }, []);

  return (
    <div>
      <h1>My Digital Wardrobe</h1>
      <ul>
        {wardrobe.map((item) => (
          <li key={item.id}>{item.name}: {item.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;