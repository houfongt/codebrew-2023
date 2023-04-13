<template>
    <div class="relative">
        <video v-show="!isPhotoTaken" ref="camera" class="w-full block" autoplay playsinline></video>
        <div class="absolute top-5 left-5 z-50">
            <p class="text-2xl text-white bg-black/50 rounded-xl py-2 px-4">Magic Meal</p>
        </div>
        <div class="absolute bottom-5 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <button class="rounded-full border-white border-solid border-[16px] p-8">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-12 h-12">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                </svg>
            </button>
        </div>
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
				video: {
                    facingMode: 'user'
                }
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