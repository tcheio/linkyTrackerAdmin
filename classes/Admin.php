<?php
class Admin {
    private $conn;
    private $table_name = "admin";

    public $id;
    public $login;
    public $password;

    public function __construct($db) {
        $this->conn = $db;
    }

    function login() {
        $query = "SELECT id, login, password FROM " . $this->table_name . " WHERE login = :login LIMIT 0,1";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':login', $this->login);
        $stmt->execute();
        $num = $stmt->rowCount();

        if ($num > 0) {
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            $this->id = $row['id'];
            $this->login = $row['username']; 
            $this->password = $row['password'];

            if (password_verify($this->password, $row['password'])) {
                return true;
            }
        }
        return false;
    }
}
?>
