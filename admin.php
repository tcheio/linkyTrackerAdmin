<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Admin Page</title>
    <link rel="stylesheet" type="text/css" href="assets/css/style.css">
    <script src="assets/js/admin.js"></script>
</head>
<body>
    <h2>Admin Page</h2>
    <table id="dataTable">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>
</body>
</html>
