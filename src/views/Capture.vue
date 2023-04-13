<template>
    <div>
         <video v-show="!isPhotoTaken" ref="camera" class="w-full h-full" autoplay></video>
    </div>
</template>

<script>
export default {
    name: 'Capture',
    data() {
        return {
            isCameraOpen: false,
            isPhotoTaken: false,
            isShotPhoto: false,
            isLoading: false,
            link: '#'
        }
    },
    mounted() {
        this.toggleCamera()
    },
    methods: {
        toggleCamera() {
            if(this.isCameraOpen) {
                this.isCameraOpen = false;
                this.isPhotoTaken = false;
                this.isShotPhoto = false;
                this.stopCameraStream();
            } else {
                this.isCameraOpen = true;
                this.createCameraElement();
            }
        },
        createCameraElement() {
            const constraints = (window.constraints = {
			    audio: false,
				video: true
			});
			navigator.mediaDevices.getUserMedia(constraints).then(stream => {
				this.$refs.camera.srcObject = stream;
			}).catch(error => {
				alert("May the browser didn't support or there is some errors.");
			});
        },
        stopCameraStream() {
            let tracks = this.$refs.camera.srcObject.getTracks();

			tracks.forEach(track => {
				track.stop();
			});
        },
    }
}
</script>

<style>

</style>