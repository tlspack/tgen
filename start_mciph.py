__author__ = 'Shirish Pal'
 
import os
import argparse
import cmds
import utils

cfj_template = '''
        {{
            "zone_label" : "zone-{zone_id}-a",
            "enable" : 1,
            "zone_type" : "single-interface",
            "iface" : "{iface}",
            "macvlan" : "{macvlan1}",
            "tcpdump" : "-c 1000",
            "subnets" : ["10.2{subnet_id}.51.0/24" , "11.2{subnet_id}.51.0/24" , "12.2{subnet_id}.51.0/24" , 
                        "13.2{subnet_id}.51.0/24" , "14.2{subnet_id}.51.0/24" , "15.2{subnet_id}.51.0/24" , 
                        "16.2{subnet_id}.51.0/24" , "17.2{subnet_id}.51.0/24" , "18.2{subnet_id}.51.0/24" , 
                        "19.2{subnet_id}.51.0/24" , "20.2{subnet_id}.51.0/24" , "21.2{subnet_id}.51.0/24" , 
                        "22.2{subnet_id}.51.0/24" , "23.2{subnet_id}.51.0/24" , "24.2{subnet_id}.51.0/24" , 
                        "25.2{subnet_id}.51.0/24" , "26.2{subnet_id}.51.0/24" , "27.2{subnet_id}.51.0/24" , 
                        "28.2{subnet_id}.51.0/24" , "29.2{subnet_id}.51.0/24" , "30.2{subnet_id}.51.0/24" , 
                        "31.2{subnet_id}.51.0/24" , "32.2{subnet_id}.51.0/24" , "33.2{subnet_id}.51.0/24" , 
                        "34.2{subnet_id}.51.0/24" , "35.2{subnet_id}.51.0/24" , "36.2{subnet_id}.51.0/24" , 
                        "37.2{subnet_id}.51.0/24" , "38.2{subnet_id}.51.0/24" , "39.2{subnet_id}.51.0/24" , 
                        "40.2{subnet_id}.51.0/24" , "41.2{subnet_id}.51.0/24" , "42.2{subnet_id}.51.0/24" , 
                        "43.2{subnet_id}.51.0/24" , "44.2{subnet_id}.51.0/24" , "45.2{subnet_id}.51.0/24" , 
                        "46.2{subnet_id}.51.0/24" , "47.2{subnet_id}.51.0/24" , "48.2{subnet_id}.51.0/24" , 
                        "49.2{subnet_id}.51.0/24"],
            "app_list" : [
                {{
                    "app_type" : "tls_client",
                    "app_label" : "AES128_SHA_CLIENT",
                    "enable" : {AES128_SHA},
                    "conn_per_sec" : {cps},
                    "max_pending_conn_count" : {max_pipeline},
                    "max_active_conn_count" : {max_active},
                    "total_conn_count" : 0,
                    "cs_grp_list" : [
                        {{
                            "cs_grp_label" : "cs_grp_1",
                            "enable" : {sslv3},
                            "srv_ip"   : "100.2{subnet_id}.51.1",
                            "srv_port" : 443,
                            "clnt_ip_begin" : "10.2{subnet_id}.51.1",
                            "clnt_ip_end" : "10.2{subnet_id}.51.10",
                            "clnt_port_begin" : 5000,
                            "clnt_port_end" : 65000,
                            "cipher" : "AES128-SHA",
                            "tls_version" : "sslv3",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "cs_grp_label" : "cs_grp_2",
                            "enable" : {tls1},
                            "srv_ip"   : "100.2{subnet_id}.51.2",
                            "srv_port" : 443,
                            "clnt_ip_begin" : "10.2{subnet_id}.51.11",
                            "clnt_ip_end" : "10.2{subnet_id}.51.20",
                            "clnt_port_begin" : 5000,
                            "clnt_port_end" : 65000,
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "cs_grp_label" : "cs_grp_3",
                            "enable" : {tls1_1},
                            "srv_ip"   : "100.2{subnet_id}.51.3",
                            "srv_port" : 443,
                            "clnt_ip_begin" : "10.2{subnet_id}.51.21",
                            "clnt_ip_end" : "10.2{subnet_id}.51.30",
                            "clnt_port_begin" : 5000,
                            "clnt_port_end" : 65000,
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1_1",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "cs_grp_label" : "cs_grp_4",
                            "enable" : {tls1_2},
                            "srv_ip"   : "100.2{subnet_id}.51.4",
                            "srv_port" : 443,
                            "clnt_ip_begin" : "10.2{subnet_id}.51.31",
                            "clnt_ip_end" : "10.2{subnet_id}.51.40",
                            "clnt_port_begin" : 5000,
                            "clnt_port_end" : 65000,
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1_2",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }}
                    ]
                }}
            ]       
        }},

        {{
            "zone_label" : "zone-{zone_id}-b",
            "enable" : 1,
            "zone_type" : "single-interface",
            "iface" : "{iface}",
            "macvlan" : "{macvlan2}",
            "tcpdump" : "-c 1000",
            "subnets" : ["100.2{subnet_id}.51.0/24" , "101.2{subnet_id}.51.0/24" , "102.2{subnet_id}.51.0/24" , 
                        "103.2{subnet_id}.51.0/24" , "104.2{subnet_id}.51.0/24" , "105.2{subnet_id}.51.0/24" , 
                        "106.2{subnet_id}.51.0/24" , "107.2{subnet_id}.51.0/24" , "108.2{subnet_id}.51.0/24" , 
                        "109.2{subnet_id}.51.0/24" , "110.2{subnet_id}.51.0/24" , "111.2{subnet_id}.51.0/24" , 
                        "112.2{subnet_id}.51.0/24" , "113.2{subnet_id}.51.0/24" , "114.2{subnet_id}.51.0/24" , 
                        "115.2{subnet_id}.51.0/24" , "116.2{subnet_id}.51.0/24" , "117.2{subnet_id}.51.0/24" , 
                        "118.2{subnet_id}.51.0/24" , "119.2{subnet_id}.51.0/24" , "120.2{subnet_id}.51.0/24" , 
                        "121.2{subnet_id}.51.0/24" , "122.2{subnet_id}.51.0/24" , "123.2{subnet_id}.51.0/24" , 
                        "124.2{subnet_id}.51.0/24" , "125.2{subnet_id}.51.0/24" , "126.2{subnet_id}.51.0/24" , 
                        "127.2{subnet_id}.51.0/24" , "128.2{subnet_id}.51.0/24" , "129.2{subnet_id}.51.0/24" , 
                        "130.2{subnet_id}.51.0/24" , "131.2{subnet_id}.51.0/24" , "132.2{subnet_id}.51.0/24" , 
                        "133.2{subnet_id}.51.0/24" , "134.2{subnet_id}.51.0/24" , "135.2{subnet_id}.51.0/24" , 
                        "136.2{subnet_id}.51.0/24" , "137.2{subnet_id}.51.0/24" , "138.2{subnet_id}.51.0/24" , 
                        "139.2{subnet_id}.51.0/24"],
            "app_list" : [
                {{
                    "app_type" : "tls_server",
                    "app_label" : "AES128_SHA_SERVER",
                    "enable" : {AES128_SHA},
                    "srv_list" : [
                        {{
                            "srv_label" : "100.2{subnet_id}.51.1",
                            "enable" : {sslv3},
                            "srv_ip" : "100.2{subnet_id}.51.1",
                            "srv_port" : 443,
                            "srv_cert" : "/rundir/certs/server.cert",
                            "srv_key" : "/rundir/certs/server.key",
                            "cipher" : "AES128-SHA",
                            "tls_version" : "sslv3",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "srv_label" : "100.2{subnet_id}.51.2",
                            "enable" : {tls1},
                            "srv_ip" : "100.2{subnet_id}.51.2",
                            "srv_port" : 443,
                            "srv_cert" : "/rundir/certs/server.cert",
                            "srv_key" : "/rundir/certs/server.key",
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "srv_label" : "100.2{subnet_id}.51.3",
                            "enable" : {tls1_1},
                            "srv_ip" : "100.2{subnet_id}.51.3",
                            "srv_port" : 443,
                            "srv_cert" : "/rundir/certs/server.cert",
                            "srv_key" : "/rundir/certs/server.key",
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1_1",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }},
                        {{
                            "srv_label" : "100.2{subnet_id}.51.4",
                            "enable" : {tls1_2},
                            "srv_ip" : "100.2{subnet_id}.51.4",
                            "srv_port" : 443,
                            "srv_cert" : "/rundir/certs/server.cert",
                            "srv_key" : "/rundir/certs/server.key",
                            "cipher" : "AES128-SHA",
                            "tls_version" : "tls1_2",
                            "close_type" : "fin",
                            "close_notify" : "no_send",
                            "write_chunk" : 1200,
                            "tcp_rcv_buff" : 0,
                            "tcp_snd_buff" : 0,
                            "cs_data_len" : 128,
                            "sc_data_len" : 128,
                            "cs_start_tls_len" : 0,
                            "sc_start_tls_len" : 0
                        }}
                    ]
                }}
            ]   
        }}
'''

def add_arguments_cb(arg_parser):
    arg_parser.add_argument('--AES128_SHA'
                                , action="store_true"
                                , default=False
                                , help = '0/1')


if __name__ == '__main__':
    CmdArgs = utils.get_arguments("mixed cipher test", add_arguments_cb)

    cfg_j_pre = '''{
        "zones" : [
'''

    cfg_j_post = '''
        ]
}'''

    cfg_j = ''
    
    for i in range(CmdArgs.zones):
        if i:
            cfg_j = cfg_j + ','
        m = vars (CmdArgs)
        m['zone_id'] = i+1
        m['subnet_id'] = i+1        
        cfg_j += cfj_template.format(**m)

    cfg_j = cfg_j_pre + cfg_j + cfg_j_post

    traffic_dir = os.path.join(CmdArgs.rundir
                                , 'traffic'
                                , CmdArgs.cfg_id)
                                
    os.system ( 'rm -rf {}'.format(traffic_dir) )
    os.system ( 'mkdir -p {}'.format(traffic_dir) )

    with open(os.path.join(traffic_dir, 'config.json'), 'w') as f:
        f.write(cfg_j)

    cmds.start_traffic(CmdArgs.cfg_id, CmdArgs.result_tag)
