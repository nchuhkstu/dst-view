import { defineConfig } from "vite";
import Vue from "@vitejs/plugin-vue";
import Components from "unplugin-vue-components/vite";
import AutoImport from "unplugin-auto-import/vite";
import {
  ElementPlusResolver,
  NaiveUiResolver
} from "unplugin-vue-components/resolvers";

export default defineConfig({
  devServer:{
    host: '0.0.0.0',
    port:3000,
    client: {
      webSocketURL: 'ws://0.0.0.0:3000/ws',
    },
    headers: {
      'Access-Control-Allow-Origin': '*',
    }
  },
  base: './',
  plugins: [

    Vue(),
    AutoImport({
      imports: ["vue", "vue-router", "pinia"]
    }),
    Components({
      resolvers: [ElementPlusResolver(), NaiveUiResolver()]
    })
  ],
});