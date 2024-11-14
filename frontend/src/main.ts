import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { provideHttpClient } from '@angular/common/http';
import { provideServerRendering } from '@angular/platform-server';

const appConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideServerRendering()
  ]
};

bootstrapApplication(AppComponent, 
  providers:[
    provideHttpClient(),
  ]
  appConfig)
  .catch((err) => console.error(err));
