"""
1. https://new.cnzz.com/v1/login.php?siteid=1280294351
2. Login with password: hass-xiaomi-miot
3. https://web.umeng.com/main.php?c=eanalysis&a=frame&siteid=1280294351#!/0/eanalysis/category/3/1280294351/2021-01-01/0
4. Search model via https://home.miot-spec.com
"""

MIOT_LOCAL_MODELS = [
    '090615.curtain.kcz82d',
    '090615.curtain.ptx82',
    '090615.curtain.sidt82',
    'ateai.mosq.dakuo',
    # 'babai.curtain.190812',  # mode/current_position return -4004
    # 'babai.curtain.bb82mj',  # mode/current_position return -4004
    'babai.switch.th01a',
    'careli.fryer.maf02',
    'cgllc.airm.cgdn1',
    'chuangmi.plug.212a01',
    'chunmi.health_pot.a1',
    'chunmi.waterpuri.800f3',
    'cubee.airrtc.th123e',
    # 'cubee.airrtc.th123w',  # issues/213
    'cuco.light.sl4',
    'cuco.plug.cp2',
    'cuco.plug.cp2a',
    'cuco.plug.cp3a',
    'cuco.plug.sp5',
    'deerma.humidifier.jsq3',
    'deerma.humidifier.jsq4',
    'deerma.humidifier.jsq5',
    'deerma.humidifier.jsqm',
    'deerma.humidifier.jsqs',
    'dmaker.airp.swift',
    'dmaker.airpurifier.f20',
    'dmaker.fan.p10',
    'dmaker.fan.p11',
    'dmaker.fan.p18',
    'dmaker.fan.p8',
    'dmaker.fan.p9',
    'dooya.curtain.m1',
    'dooya.curtain.m2',
    'dreame.vacuum.mb1808',
    'dreame.vacuum.mc1808',
    'dreame.vacuum.p2008',
    'dreame.vacuum.p2009',
    'dreame.vacuum.p2029',
    'dreame.vacuum.p2036',
    'dreame.vacuum.p2041',
    'dreame.vacuum.p2157',
    'dreame.vacuum.p2259',  # issues/222
    'ijai.vacuum.v2',
    'isa.camera.hlc7',
    'julun.switch.jlsw01',
    'kejia.airer.mznpro',
    'leishi.light.eps112',
    'leishi.light.eps118',
    'linp.switch.q31',
    'linp.switch.q32',
    'lumi.acpartner.mcn04',
    'lumi.airer.acn02',
    'lumi.curtain.hagl05',
    'lumi.curtain.hmcn01',
    'midjd6.fridge.v1',
    'mijia.vacuum.v1',
    'mijia.vacuum.v2',
    'mmgg.pet_waterer.s1',
    'mrbond.airer.m2',
    'opple.light.tabcw',
    'philips.light.cbulb',
    'philips.light.dlight',
    'qushui.bed.003',
    'roidmi.vacuum.v60',
    'szdy.airfresh.n80',
    'uvfive.s_lamp.slmap2',
    'viewx.light.101001',
    'viomi.bhf_light.v4',
    'viomi.dishwasher.v06',
    'viomi.fan.v6',
    'viomi.hood.v2',
    'viomi.vacuum.v13',
    'viomi.vacuum.v15',
    'viomi.vacuum.v17',
    'viomi.vacuum.v18',
    'viomi.vacuum.v19',
    'viomi.washer.v19',
    'xiaomi.aircondition.c12',
    'xiaomi.aircondition.c16',
    'xiaomi.aircondition.mc5',
    'xiaomi.aircondition.mc7',
    'xiaomi.aircondition.mc8',
    'xiaomi.aircondition.mh1',
    'xiaomi.aircondition.mh2',
    'xiaomi.aircondition.mt1',
    'xiaomi.aircondition.mt2',
    'xiaomi.aircondition.mt3',
    'xiaomi.aircondition.mt4',
    'xiaomi.aircondition.mt6',
    'xiaomi.aircondition.mt7',
    'xiaomi.aircondition.mt8',
    'yeelink.bhf_light.v6',
    'yeelink.curtain.ctmt1',
    'yeelink.light.ceil26',
    'yeelink.light.ceilb',
    'yeelink.light.ceilc',
    'yeelink.light.colorc',
    'yeelink.light.fancl2',
    'yeelink.light.lamp15',
    'yeelink.light.mono6',
    'yeelink.light.monob',
    'yeelink.light.stripa',
    'yeelink.switch.sw1',
    'ymt.flowerpot.v1',
    'yunmi.waterpuri.f7',
    'zdeer.foot_bath.zdz9',
    'zhimi.airfresh.ua1',
    'zhimi.airpurifier.ma4',
    'zhimi.airpurifier.mb3',
    'zhimi.airpurifier.mb4',
    'zhimi.airpurifier.vb2',
    'zhimi.airpurifier.xa1',
    'zhimi.airpurifier.za1',
    'zhimi.fan.fa1',
    'zhimi.fan.fb1',
    'zhimi.fan.za5',
    'zhimi.heater.ma3',
    'zhimi.heater.za2',
    'zhimi.humidifier.ca4',
    'zhimi.humidifier.va1',
    'zhimi.vacuum.xa1',
]