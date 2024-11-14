import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideServerRendering } from '@angular/platform-server';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';

const config = {
  providers: [
    provideServerRendering(),
    provideRouter(routes)
  ]
};

const bootstrap = () => bootstrapApplication(AppComponent, config);

export default bootstrap;
