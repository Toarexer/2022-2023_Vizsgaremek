<?php
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpdb' );
/** Database username */
define( 'DB_USER', 'dbuser' );
/** Database password */
define( 'DB_PASSWORD', 'dbpass' );
/** Database hostname */
define( 'DB_HOST', 'mariadb' );
/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );
/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

define('AUTH_KEY',         'cQIZOl[ToY{gQ-j+*c5DS^?RzbPtv_2!~*A2-0z+%q~H@teN$Yv*HT[^|1c{c7-3');
define('SECURE_AUTH_KEY',  'RwzJIuO074G$yWh}xa[0|aW/@6${Byq4L2,X<|+P>l|lMu/j(iF%>sSloEVitI$8');
define('LOGGED_IN_KEY',    '3`+=3DUH#mAj-ebw&rpR4:lSll}NLRof>M}RHkub=)@)<qU|o6+V]sBmE>[AXnxx');
define('NONCE_KEY',        'S%8p1.#Una$EnF/7+Ob-LeKtKP*|yC%9}s<WDJ^CKA*aE>7*?`/ {;&~SO26n.Ej');
define('AUTH_SALT',        '.v?P{rO[Ac&b}LLp_KwxpR-eOt~:XI^6$z+(VutQAj}#XZA*ROHuR|Pfz[v{57Y;');
define('SECURE_AUTH_SALT', '+0n+-E6=pKK]w-wSAPCrGg)Jge+-3pPO)/dJy&]9Y(.s$sh19g-z;@hdcu|u&%<!');
define('LOGGED_IN_SALT',   'wKA{Is>;2IDV2.<YM(f-l/ha_HeSfOude$$-?UE%o~+M((|FW|rR*/dp%aTP[NGJ');
define('NONCE_SALT',       'iK<:*G|n`A89j:=]7Qw^hhH2a6#:Xye-;<|9p?j@.4*<A-lC#1h WyFyWMV%]W[c');

$table_prefix = 'wp_';

define( 'WP_DEBUG', false );

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
