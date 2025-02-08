/* import { useState } from "react";
import Papa from "papaparse";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const DataVisualization = () => {
  const [data, setData] = useState([]);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    Papa.parse(file, {
      header: true,
      dynamicTyping: true,
      complete: (result) => {
        setData(result.data);
      },
    });
  };

  return (
    <div>
      <h1>CSV Data Visualization</h1>
      <input type="file" accept=".csv" onChange={handleFileUpload} />
      
      {data.length > 0 && (
        <LineChart width={600} height={300} data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="yourXColumn" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="yourYColumn" stroke="#8884d8" />
        </LineChart>
      )}
    </div>
  );
};

export default DataVisualization; */
