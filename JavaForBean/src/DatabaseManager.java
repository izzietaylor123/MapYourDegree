import java.sql.*;

public class DatabaseManager {
  private static final String URL = "jdbc:mysql://localhost:3306/DegreeProgress";
  private static final String USER = "root";
  private static final String PASSWORD = "Me0wmeow";
  private Connection connection;

  public DatabaseManager() {
    try {
      connection = DriverManager.getConnection(URL, USER, PASSWORD);
      System.out.println("Connected to the database.");
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }

  public Connection getConnection() {
    return connection;
  }

  public void closeConnection() {
    try {
      if (connection != null) connection.close();
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }
}
