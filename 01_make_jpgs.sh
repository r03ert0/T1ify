orientations=( x y z )

mkdir -p jpgs

# nOK=0
# find t2w/*/*/ -name *.nii.gz|while read t2; do
#     dim=$(./volume/volume -i $t2 -info|grep dim|awk -F' ' '{print $4}')
#     if (( dim == 256 )); then
#         sub=$(echo $t2|awk -F'/' '{print $2}')
#         t1=$(find t1w/$sub -name *.nii.gz -print -quit)
#         if [ -f "$t1" ]; then
#             nOK=$(( nOK + 1 ))
#             echo $sub is OK $nOK
#         fi
#     else
#         echo $t2 has zdim=$dim
#     fi
# done

find t2w/*/*/ -name *.nii.gz|while read t2; do
    dim=$(./volume/volume -i $t2 -info|grep dim|awk -F' ' '{print $4}')
    if (( dim == 256 )); then
        sub=$(echo $t2|awk -F'/' '{print $2}')
        echo $sub $dim $t2
        find t1w/$sub -name *.nii.gz -print -quit|while read t1; do
            # now we have a good t2w and a good t1w
            # let's make 20 jpgs

            for ((i=0;i<20;i++)); do
                # random orientation
                ori=${orientations[ $(( RANDOM % 3 )) ]}

                # random position
                pos=$(awk -v R=$RANDOM 'BEGIN{print R/32767.0}')

                ./volume/volume -i $t2 -tiff jpgs/t2w_${sub}_${i}.tif,grey,$ori,$pos
                convert jpgs/t2w_${sub}_${i}.tif jpgs/t2w_${sub}_${i}.jpg
                rm jpgs/t2w_${sub}_${i}.tif
                ./volume/volume -i $t1 -tiff jpgs/t1w_${sub}_${i}.tif,grey,$ori,$pos
                convert jpgs/t1w_${sub}_${i}.tif jpgs/t1w_${sub}_${i}.jpg
                rm jpgs/t1w_${sub}_${i}.tif
            done
        done
    fi
done