import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.jepsc.codebrew23',
  appName: 'magic-meal',
  webDir: 'dist',
  bundledWebRuntime: false,
  "server": {
    "url": "https://aesthetic-marshmallow-71934e.netlify.app/",
    "cleartext": true
  },
};

export default config;
