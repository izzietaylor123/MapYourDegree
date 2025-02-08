import './DegreeResults.css';
import { useState, useEffect } from "react";

function DegreeResults() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("./Business_admin_and_law-BS-Business Cooperative Education .json") // Change to match your JSON filename
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error("Error loading JSON:", error));
  }, []);

  return (
    <div className="degree-container">
      <h2>Degree Courses</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Course Code</th>
            <th>Course Name</th>
            <th>Course Hours</th>
            <th>Requirement Group</th>
            <th>Number Required</th>
            <th>Enrolled</th>
          </tr>
        </thead>
        <tbody>
          {data.map((course, index) => (
            <tr key={index}>
              <td>{course["Course Code"]}</td>
              <td>{course["Course Name"]}</td>
              <td>{course["Course Hours"]}</td>
              <td>{course["Requirement Group"]}</td>
              <td>{course["Number Required"]}</td>
              <td>{course["Enrolled"]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DegreeResults;

