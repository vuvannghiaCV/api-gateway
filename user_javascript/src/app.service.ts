import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello() {
    return {
      language: 'javascript',
      message: `Hello World from ${process.env.SERVICE_NAME}`,
    };
  }
  healthCheck() {
    return {
      language: 'javascript',
      message: `Health check from ${process.env.SERVICE_NAME}`,
    };
  }
}
