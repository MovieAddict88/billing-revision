<?php
session_start();
require_once 'config/dbconnection.php';
require_once 'includes/classes/admin-class.php';

$dbh = new Dbconnect();
$admins = new Admins($dbh);

$is_admin = isset($_SESSION['admin_session']) && $_SESSION['admin_session']->role == 'admin';
$employer_id = isset($_SESSION['admin_session']) ? $_SESSION['admin_session']->user_id : null;

$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$limit = isset($_GET['limit']) ? (int)$_GET['limit'] : 10;
$q = isset($_GET['q']) ? $_GET['q'] : null;

$offset = ($page - 1) * $limit;

if ($is_admin) {
    $results = $admins->fetchDisconnectedCustomersPage($offset, $limit, $q);
    $total_records = $admins->countDisconnectedCustomers($q);
} else {
    $results = $admins->fetchDisconnectedCustomersByEmployerPage($employer_id, $offset, $limit, $q);
    $total_records = $admins->countDisconnectedCustomersByEmployer($employer_id, $q);
}

$total_pages = ceil($total_records / $limit);
$packages = $admins->getPackages();

if (isset($results) && sizeof($results) > 0) {
    foreach ($results as $result) {
        $package_name = '';
        foreach ($packages as $package) {
            if ($package->id == $result->package_id) {
                $package_name = $package->name;
                break;
            }
        }
?>
        <tr>
            <td><?= $result->id ?></td>
            <td><?= $result->full_name ?></td>
            <?php if ($is_admin) : ?>
                <td><?= $result->employer_name ?></td>
            <?php endif; ?>
            <td><?= $result->nid ?></td>
            <td><?= $result->address ?></td>
            <td><?= $package_name ?></td>
            <td><?= $result->ip_address ?></td>
            <td><?= $result->email ?></td>
            <td><?= $result->contact ?></td>
            <td><?= $result->conn_type ?></td>
            <td><span class="label label-danger"><?= $result->status ?></span></td>
            <td><?= $result->login_code ?></td>
            <td><?= $result->due_date ?></td>
            <td><?= $result->remarks ?></td>
        </tr>
    <?php }
} else { ?>
    <tr>
        <td colspan="<?= $is_admin ? '15' : '14' ?>" align="center">No disconnected clients found</td>
    </tr>
<?php }

if ($total_pages > 1) { ?>
    <tr class="pagination-row" data-page="<?= $page ?>" data-total="<?= $total_records ?>" data-limit="<?= $limit ?>" data-query="<?= $q ?>">
        <td colspan="<?= $is_admin ? '15' : '14' ?>" align="center">
            <ul class="pagination">
                <?php if ($page > 1) : ?>
                    <li><a href="#" class="page-prev">&laquo;</a></li>
                <?php endif; ?>
                <?php for ($i = 1; $i <= $total_pages; $i++) : ?>
                    <li class="<?= ($i == $page) ? 'active' : '' ?>"><a href="#" class="page-num"><?= $i ?></a></li>
                <?php endfor; ?>
                <?php if ($page < $total_pages) : ?>
                    <li><a href="#" class="page-next">&raquo;</a></li>
                <?php endif; ?>
            </ul>
        </td>
    </tr>
<?php }
