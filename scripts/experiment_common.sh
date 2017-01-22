
function create_experiment_set_variables {
    readonly EXTERNAL_DRIVE=/video-drive1/salsify-results
    readonly INTERNAL_DRIVE=/video-drive2
    
    readonly EXPERIMENT_VIDEO_NAME=$(basename $1)
    readonly EXPERIMENT_VIDEO_PATH=$(readlink -m $(dirname $1))
    
    readonly EXPERIMENT_DIR=$EXPERIMENT_VIDEO_PATH/$EXPERIMENT_VIDEO_NAME
    if [[ -d $EXPERIMENT_DIR || -f $EXPERIMENT_DIR ]]; then
	echo "Experiment dir already exists!"
	echo "run 'remove_experiment $1' to remove all files related to this experiment"
	exit -1
    fi
    
    echo $EXPERIMENT_DIR
    readonly RESULTS_DIR=$(echo $EXPERIMENT_DIR | awk -F"salsify-results/benchmarks"  '{print $2}')
    echo $RESULTS_DIR
    if [[ -z $RESULTS_DIR ]]; then
	echo "Experments must be in the salsify-results/benchmarks dir"
	exit -1
    fi

    if [[ -d $RESULTS_DIR || -f $RESULTS_DIR ]]; then
	echo "Results dir already exists!"
	echo "run 'remove_experiment $1' to remove all files related to this experiment"
	exit -1
    fi
    
    export EXTERNAL_DRIVE
    export INTERNAL_DRIVE
    export EXPERIMENT_VIDEO_NAME
    export EXPERIMENT_VIDEO_PATH
    export RESULTS_DIR
}

function remove_experiment_set_variables {
    readonly EXTERNAL_DRIVE=/video-drive1/salsify-results
    readonly INTERNAL_DRIVE=/video-drive1
    
    readonly EXPERIMENT_VIDEO_NAME=$(basename $1)
    readonly EXPERIMENT_VIDEO_PATH=$(readlink -m $(dirname $1))
    
    readonly EXPERIMENT_DIR=$EXPERIMENT_VIDEO_PATH/$EXPERIMENT_VIDEO_NAME
    readonly RESULTS_DIR=$(echo $EXPERIMENT_DIR | awk -F"salsify-results/benchmarks/"  '{print $2}') 
    
    export EXTERNAL_DRIVE
    export INTERNAL_DRIVE
    export EXPERIMENT_VIDEO_NAME
    export EXPERIMENT_VIDEO_PATH
    export RESULTS_DIR
}

