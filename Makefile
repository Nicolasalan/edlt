DOCKER_VOLUMES = \
	--volume="$(shell pwd)/src":"/ws":rw \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--volume="${HOME}/.Xauthority:/root/.Xauthority:rw" 


DOCKER_ENV_VARS = \
	--env="DISPLAY" \
	--env="QT_X11_NO_MITSHM=1"

DOCKER_ARGS = ${DOCKER_VOLUMES} ${DOCKER_ENV_VARS}
	
define xhost_activate
	@echo "Enabling local xhost sharing:"
	@echo "  Display: ${DISPLAY}"
	@xhost local:root
endef

# === Build Docker Image ===
.PHONY: build
build:
	@docker build -t dev .

# === Terminal Debugging ===
.PHONY: term
term:
	@docker run -it --net=host ${DOCKER_ARGS} dev bash

# === Distribution Normalization ===
.PHONY: norm
norm:
	@sudo xhost +
	@docker run -it --net=host ${DOCKER_ARGS} dev bash -c "cd src/statistic/normal && python3 norm.py"

# === Sampling ===
.PHONY: sample
sample:
	@docker run -it--net=host ${DOCKER_ARGS} dev bash -c "cd src/statistic/sampling && python3 sample.py"


# ========= VIBRATION =========

# === Frequency Analysis ===
.PHONY: freq
freq:
	@docker run -it--net=host ${DOCKER_ARGS} dev bash -c "cd src/vibration/frequency && python3 main.py"

