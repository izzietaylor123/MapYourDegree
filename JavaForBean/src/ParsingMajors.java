import java.io.*;
import java.util.*;

public class ParsingMajors {

  public static List<String> parseMajors(String filePath) {
    List<String> formattedData = new ArrayList<>();
    String line;

    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      br.readLine(); // Skip header row

      while ((line = br.readLine()) != null) {
        String[] values = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"); // Handles quoted commas

        if (values.length >= 3) {
          String transcriptTitle = values[1].replace("\"", "").trim();
          String cipCode = values[2].replace("\"", "").trim();

          // Format as required: Major CIP Code, "Major Transcript Title"
          String formatted = "INSERT INTO Majors (major_id, major_name) VALUES ("
                  + cipCode + ", " + "'"+transcriptTitle+"'"+")";

          formattedData.add(formatted);
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    return formattedData;
  }

  // Method to insert the parsed data into the database
  protected String getDataBaseString(String cipCode, String majorName) {
    String sql = "INSERT INTO Majors (major_id, major_name) VALUES (?, ?)";
    return sql;
  }
}
