import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ParsingClasses {
  public static List<String> parseCourses(String filePath) {
    List<String> formattedData = new ArrayList<>();
    String line;

    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      br.readLine(); // Skip header row

      while ((line = br.readLine()) != null) {
        String[] values = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"); // Handles quoted commas

        if (values.length >= 7) { // Ensure all necessary columns exist
          String courseId = values[0].trim().replace("\"", "");  // Course ID (e.g., "CS 4730")
          String courseName = values[1].trim().replace("\"", ""); // Course Name (e.g., "Distributed Systems")

          // Handle credits (set NULL if missing)
          String credits = values[2].trim();
          if (credits.isEmpty()) {
            credits = "NULL";
          }

          // Handle category conversion
          String category = values[3].trim();
          if (category.equalsIgnoreCase("Default1")) {
            category = "'Major'";
          } else if (category.equalsIgnoreCase("NUPath")) {
            category = "'NUPath'";
          } else {
            category = "'Elective'";
          }

          // Handle num_required as ENUM ('1', '2', '3', '5', 'All')
          String numRequired = values[4].trim();
          if (!numRequired.matches("1|2|3|5|All")) {
            numRequired = "'All'"; // Default to 'All' if invalid
          } else {
            numRequired = "'" + numRequired + "'";
          }

          // Extract offered semester
          String offeredSemester = values[5].trim();
          if (offeredSemester.isEmpty()) {
            offeredSemester = "NULL"; // Set to NULL if missing
          } else {
            offeredSemester = "'" + offeredSemester + "'";
          }

          // Extract taken status
          String taken = values[6].trim();
          if (taken.equalsIgnoreCase("True")) {
            taken = "TRUE";
          } else {
            taken = "FALSE"; // If missing or incorrect, default to FALSE
          }

          // Insert statement for Courses table
          String formatted = "INSERT INTO Courses (course_id, course_name, credits, category, num_required, offered_semester, taken) VALUES ('"
                  + courseId + "', '" + courseName + "', " + credits + ", " + category + ", " + numRequired + ", " + offeredSemester + ", " + taken + ");";

          formattedData.add(formatted);
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    return formattedData;
  }
}
