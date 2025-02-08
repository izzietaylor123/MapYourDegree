import './DegreeResults.css';

function DegreeResults() {
<div>
      <h2>Degree Programs</h2>
      <input 
        type="text" 
        placeholder="Enter Degree Page URL" 
        value={url} 
        onChange={(e) => setUrl(e.target.value)}
      />
      <button onClick={fetchData}>Fetch Degrees</button>

      {data.length > 0 ? (
        <table border="1">
          <thead>
            <tr>
              <th>Title</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {data.map((degree, index) => (
              <tr key={index}>
                <td>{degree.title}</td>
                <td>{degree.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No data yet. Enter a URL and click "Fetch Degrees".</p>
      )}
    </div>
  );
}
}
