import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.jepsc.codebrew23',
  appName: 'Meal Magic',
  webDir: 'dist',
  bundledWebRuntime: false,
  "server": {
    "url": "https://codebrew.cgps.ch/",
    "cleartext": true
  },
};

export default config;
