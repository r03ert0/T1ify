echo jpgs/*.jpg|xargs ls|while read g; do
    d=$(dirname $g)
    f=$(basename $g)
    read seq sub num < <(echo $f|awk -F'_' '{printf "%s %s_%s_%s %i",$1,$2,$3,$4,$5}')
    if [ $seq == "t1w" ]; then
        if [ ! -f "$d/t2w_"$sub"_"$num".jpg" ]; then
            echo "Removing $d/$f, which had t1w but not t2w"
            rm $d/t1w_${sub}_$num.jpg
        fi
    else
        if [ ! -f "$d/t1w_"$sub"_"$num".jpg" ]; then
            echo "Removing $d/$f, which had t2w but not t1w"
            rm $d/t2w_${sub}_$num.jpg
        fi
    fi
done