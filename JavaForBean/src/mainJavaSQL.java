import java.sql.*;
import java.util.*;

public class mainJavaSQL {
  public static void main(String[] args) {
    DatabaseManager connection = new DatabaseManager();
    List<String> parsedData = ParsingMajors.parseMajors("northeastern-majors.csv");
    insertDataIntoDB(connection.getConnection(), parsedData);
  }

  public static void insertDataIntoDB(Connection connection, List<String> parsedData) {
    for (String query : parsedData) {
      try (Statement stmt = connection.createStatement()) {
        System.out.println(query);
        stmt.executeUpdate(query);
      } catch (SQLException e) {
        e.printStackTrace();
        throw new RuntimeException(e);
      }
    }
  }

}
