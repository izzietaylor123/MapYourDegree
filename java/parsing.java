import java.io.*;
import java.util.*;

class CSVParser {
  List<DataRecord> records = parseCSV(filePath);

  public static List<DataRecord> parseCSV(String filePath) {
    List<DataRecord> records = new ArrayList<>();
    String line;

    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      br.readLine(); // Skip header if present

      while ((line = br.readLine()) != null) {
        String[] values = line.split(",");
        if () {
          Record record = new Record(values[0], values[1], values[2]);
          records.add(record);
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    return records;
  }


  @Override
  public String toString() {
    return "";
  }
}