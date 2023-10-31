_base_ = '/home/di.tong/mmrotate-main/configs/rotated_retinanet/rotated_retinanet_hbb_r50_fpn_1x_dota_oc.py'
#_base_ = '/home/di.tong/mmrotate-main/configs/redet/redet_re50_refpn_1x_dota_le90.py'
data_root = 'data/Drilling_platforms1280/'
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=0,
    train=dict(
        type='DOTADataset',
        ann_file="data/Drilling_platforms1280/dotalable/",
        img_prefix="data/Drilling_platforms1280/img/",
        ),
    val=dict(
        type='DOTADataset',
        ann_file="data/Drilling_platforms1280/dotalable/",
        img_prefix="data/Drilling_platforms1280/img/",
        ),
    test=dict(
        type='DOTADataset',
        ann_file="data/Drilling_platforms1280/test/label/",
        img_prefix="data/Drilling_platforms1280/test/img/",
        ),
)
runner = dict(type='EpochBasedRunner', max_epochs=500)

