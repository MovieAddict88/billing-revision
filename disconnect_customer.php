<?php
require_once 'includes/headx.php';
require_once 'config/dbconnection.php';
$dbh = new Dbconnect();
require_once "includes/classes/admin-class.php";
$admins = new Admins($dbh);

if (isset($_GET['customer_id'])) {
    $customer_id = $_GET['customer_id'];
    $admins->disconnectCustomer($customer_id);
}

header("Location: customers.php");
exit();
