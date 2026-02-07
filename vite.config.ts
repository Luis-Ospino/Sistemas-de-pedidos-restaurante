import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

const allowedHosts = [".trycloudflare.com", "localhost", "127.0.0.1", "::1"];

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  server: {
    allowedHosts,
  },
});
