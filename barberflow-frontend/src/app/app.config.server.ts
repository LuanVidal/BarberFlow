import { mergeApplicationConfig, ApplicationConfig } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { appConfig } from './app.config'; // Importa a config do cliente

const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering() // <--- OBRIGATÓRIO PARA SSR
  ]
};

// Funde as duas configurações (Cliente + Servidor)
export const config = mergeApplicationConfig(appConfig, serverConfig);