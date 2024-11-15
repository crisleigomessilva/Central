import { EnvironmentProviders, importProvidersFrom } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const config: EnvironmentProviders[] = [
  provideServerRendering(),
  provideRouter(routes),
];
